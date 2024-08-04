#!/usr/bin/env bash

declare -A anitya_ids=(
	["7zip/7zip.spec"]=368867
	["bandwhich/bandwhich.spec"]=236376
	["btdu/btdu.spec"]=372783
	["cliphist/cliphist.spec"]=242870
	["croc/croc.spec"]=350834
	["doggo/doggo.spec"]=373317
	["du-dust/du-dust.spec"]=141344
	["git-graph/git-graph.spec"]=372785
	["hwatch/hwatch.spec"]=372787
	["iamb/iamb.spec"]=372778
	["klassy/klassy.spec"]=372810
	["kwin-effects/kwin-effects-sliding-notifications.spec"]=372805
	["mergerfs/mergerfs.spec"]=372789
	["niri/niri.spec"]=372826
	["onefetch/onefetch.spec"]=141703
	["par2cmdline-turbo/par2cmdline-turbo.spec"]=372791
	["prismlauncher/prismlauncher.spec"]=301949
	["ripdrag/ripdrag.spec"]=372793
	["rofi-emoji/rofi-emoji.spec"]=242096
	["rust-keyframe/rust-keyframe.spec"]=373513
	["rust-keyframe_derive/rust-keyframe_derive.spec"]=373520
	["rust-libvips/rust-libvips.spec"]=373523
	["rust-spin_sleep/rust-spin_sleep.spec"]=242190
	["satty/satty.spec"]=372795
	["swaylock-effects/swaylock-effects.spec"]=312399
	["swaync/swaync.spec"]=242061
	["try/try.spec"]=372797
	["vesktop/vesktop.spec"]=372800
	["walker/walker.spec"]=372963
	["wallust/wallust.spec"]=372803
	["wl-restart/wl-restart.spec"]=373511
	["wl-screenrec/wl-screenrec.spec"]=373536
	["yazi/yazi.spec"]=370571
)

declare -A git_forges=(
	["hsize/hsize.spec"]=github
	["overmask/overmask.spec"]=github
	["quickshell/quickshell.spec"]=github
	["try/try-git.spec"]=github
	["xwayland-satellite/xwayland-satellite.spec"]=github
)

for file in "${!anitya_ids[@]}"; do
	name=$(sed -n "s|^Name:\s\+\(.*\)$|\1|p" "$file" | head -1)
	echo "> querying versions for $name ($file)..."

	if ! api_response=$(curl -fsSL "https://release-monitoring.org/api/v2/versions/?project_id=${anitya_ids[$file]}") ||
		[[ -z "$api_response" ]]; then
		echo -e "couldn't query anitya api for $name! api response: $api_response"
		continue
	fi

	if ! latest_version=$(echo "$api_response" | jq -r .latest_version) || [[ -z "$latest_version" ]]; then
		echo -e "couldn't parse versions for $name! api response: $api_response"
		continue
	fi

	latest_version=${latest_version//-/\~}
	current_version=$(sed -n "s|^Version:\s\+\(.*\)$|\1|p" "$file" | head -1)

	if [[ "$current_version" != "$latest_version" ]]; then
		if (git log -1 --pretty="format:%B" "$file" | grep -qE "^update.sh: override.*$latest_version.*$"); then
			echo "ignoring $latest_version for $name as it has been manually overridden"
			continue
		fi

		echo "$name is not up-to-date ($current_version -> $latest_version)! modifying attributes..."
		sed -i "s|^Version:\(\s\+\)$current_version$|Version:\1$latest_version|" "$file"
		sed -i "s|^Release:\(\s\+\)[0-9]\+%{?dist}|Release:\11%{?dist}|" "$file"

		git add "$file"
		git commit -m "$name: $current_version -> $latest_version"
	fi
done

for file in "${!git_forges[@]}"; do
	name=$(sed -n "s|^Name:\s\+\(.*\)$|\1|p" "$file" | head -1)
	echo "> querying commits for $name ($file)..."

	current_commit=$(sed -n "s|^%global\s\+commit\s\+\(.*\)$|\1|p" "$file" | head -1)
	current_snapdate=$(sed -n "s|^%global\s\+snapdate\s\+\(.*\)$|\1|p" "$file" | head -1)

	case ${git_forges[$file]} in
	github)
		url=$(sed -n "s|^URL:\s\+\(.*\)$|\1|p" "$file" | head -1)
		owner_repo=$(echo "$url" | sed -n "s|^https://github.com/\(.*\)$|\1|p")

		if ! api_response=$(curl -fsSL "https://api.github.com/repos/$owner_repo/commits") ||
			[[ -z "$api_response" ]]; then
			echo -e "couldn't query github api for $name! api response: $api_response"
			continue
		fi

		if ! latest_commit=$(echo "$api_response" | jq -r ".[0].sha") || [[ -z "$latest_commit" ]]; then
			echo -e "couldn't parse commit hash for $name! api response: $api_response"
			continue
		fi

		if ! latest_snapdate=$(date +"%Y%m%d" -d"$(echo "$api_response" | jq -r ".[0].commit.committer.date")") ||
			[[ -z "$latest_snapdate" ]]; then
			echo -e "couldn't parse commit date for $name! api response: $api_response"
			continue
		fi

		if [[ "$current_commit" != "$latest_commit" ]]; then
			update_message="$current_commit @ $current_snapdate -> $latest_commit @ $latest_snapdate"
			echo "$name is not up-to-date ($update_message)! modifying attributes..."

			sed -i "s|^%global\(\s\+\)commit\(\s\+\)$current_commit$|%global\1commit\2$latest_commit|" "$file"
			sed -i "s|^%global\(\s\+\)snapdate\(\s\+\)$current_snapdate$|%global\1snapdate\2$latest_snapdate|" "$file"

			git add "$file"
			git commit -m "$name: update" -m "$update_message"
		fi
		;;
	esac
done

echo "> updating submodules..."
git submodule update --recursive --remote --init
if [[ "$(git status -s)" ]]; then
	modified_submodules=$(git diff --name-status | grep "^M" | cut -f2 | cut -d'/' -f1)
	git add .
	git commit -m "treewide: update submodules"
fi

git pull
git push

if [[ -n "$modified_submodules" ]] && [[ -n "$COPR_API_CREDENTIALS" ]]; then
	echo "> triggering copr builds..."

	pip install copr-cli
	echo -e "$COPR_API_CREDENTIALS" >~/.config/copr

	for package in $modified_submodules; do
		~/.local/bin/copr-cli build-package errornointernet/packages --nowait --name "$package"
	done
fi
