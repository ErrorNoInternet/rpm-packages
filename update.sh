#!/usr/bin/env bash

allow=(
    "./btdu/btdu.spec"
    "./cliphist/cliphist.spec"
    "./git-graph/git-graph.spec"
    "./hwatch/hwatch.spec"
    "./iamb/iamb.spec"
    "./klassy/klassy.spec"
    "./kwin-effects/kwin-effects-sliding-notifications.spec"
    "./mergerfs/mergerfs.spec"
    "./onefetch/onefetch.spec"
    "./par2cmdline-turbo/par2cmdline-turbo.spec"
    "./prismlauncher/prismlauncher.spec"
    "./ripdrag/ripdrag.spec"
    "./satty/satty.spec"
    "./stylua/stylua.spec"
    "./swaync/swaync.spec"
    "./try/try.spec"
    "./vesktop/vesktop.spec"
    "./yazi/yazi.spec"
)
modified=false

for file in $(find . -type f -name "*.spec"); do
    if [[ ! " ${allow[*]} " =~ " ${file} " ]]; then continue; fi

    url=$(sed -n "s|^URL:\s\+\(.*\)$|\1|p" "$file")
    repository=$(echo "$url" | sed -n 's|.*github.com/\(.*\)$|\1|p')
    api_response=$(curl -s "https://api.github.com/repos/$repository/releases/latest")
    if [[ $? -ne 0 ]]; then
        echo "[!] failed to request latest version for $repository!"
        echo -e "api response:\n$api_response"
        continue
    fi

    latest_version=$(echo "$api_response" | grep tag_name | sed -n 's|.*".*": "\(.*\)".*|\1|p' | sed 's|^v||')
    if [[ -z "$latest_version" ]]; then
        echo "[!] failed to request latest version for $repository!"
        echo -e "api response:\n$api_response"
        continue
    fi
    version=$(sed -n "s|^Version:\s\+\(.*\)$|\1|p" "$file")

    if [[ "$version" != "$latest_version" ]]; then
        echo "[!] $file is not up-to-date ($version -> $latest_version)"

        echo "modifying attributes in file..."
        sed -i "s|^Version:\(\s\+\)$version|Version:\1$latest_version|" "$file"
        sed -i "s|^Release:\(\s\+\)[0-9]\+%{?dist}|Release:\11%{?dist}|" "$file"

        echo "running git add && git commit..."
        git add "$file"
        git commit -m "$repository: $version -> $latest_version"

        modified=true
        echo "successfully updated $file ($version -> $latest_version)"
    else
        echo "$file is up-to-date ($latest_version)"
    fi
done

echo "updating submodules..."
git submodule update --remote --recursive
if [[ $(git status -z) ]]; then
    echo "running git add && git commit..."
    git add .
    git commit -m "treewide: update submodules"

    modified=true
fi

if [[ $modified = true ]]; then
    echo "running git push..."
    git push
fi
