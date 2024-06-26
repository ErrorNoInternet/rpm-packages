#!/usr/bin/env bash

declare -A package_ids=(
	["7zip/7zip.spec"]=368867
	["btdu/btdu.spec"]=372783
	["cliphist/cliphist.spec"]=242870
	["croc/croc.spec"]=350834
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
	["rust-du-dust/rust-du-dust.spec"]=141344
	["satty/satty.spec"]=372795
	["swaylock-effects/swaylock-effects.spec"]=312399
	["swaync/swaync.spec"]=242061
	["try/try.spec"]=372797
	["vesktop/vesktop.spec"]=372800
	["walker/walker.spec"]=372963
	["wallust/wallust.spec"]=372803
	["yazi/yazi.spec"]=370571
)

for package_file in "${!package_ids[@]}"; do
	package_name=$(sed -n "s|^Name:\s\+\(.*\)$|\1|p" "$package_file" | head -1)
	echo "> querying versions for $package_name ($package_file)..."

	if ! api_response=$(curl -fsSL "https://release-monitoring.org/api/v2/versions/?project_id=${package_ids[$package_file]}") ||
		[[ -z "$api_response" ]]; then
		echo -e "couldn't query api for $package_name! api response: $api_response"
		continue
	fi

	if ! latest_version=$(echo "$api_response" | jq -r .latest_version) || [[ -z "$latest_version" ]]; then
		echo -e "couldn't parse versions for $package_name! api response: $api_response"
		continue
	fi

	latest_version=${latest_version//-/\~}
	current_version=$(sed -n "s|^Version:\s\+\(.*\)$|\1|p" "$package_file" | head -1)

	if [[ "$current_version" != "$latest_version" ]]; then
		echo "$package_name is not up-to-date ($current_version -> $latest_version)! modifying attributes..."

		sed -i "s|^Version:\(\s\+\)$current_version$|Version:\1$latest_version|" "$package_file"
		sed -i "s|^Release:\(\s\+\)[0-9]\+%{?dist}|Release:\11%{?dist}|" "$package_file"

		git add "$package_file"
		git commit -m "$package_name: $current_version -> $latest_version"
	fi
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
