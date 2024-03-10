#!/usr/bin/env bash

modified=false
ignore=(
    "./7zip/7zip.spec"
    "./LightlyShaders/LightlyShaders.spec"
    "./timg/timg.spec"
)

for file in $(find . -type f -name "*.spec"); do
    if [[ " ${ignore[*]} " =~ " ${file} " ]]; then
        echo "ignoring $file!"
        continue
    fi

    url=$(grep "URL: " "$file" | cut -d' ' -f2)
    repository=$(echo "$url" | sed -n 's|.*github.com/\(.*\)$|\1|p')
    api_response=$(curl -s "https://api.github.com/repos/$repository/releases/latest")
    if [[ $? -ne 0 ]]; then
        echo "failed to request latest version for $repository!"
        echo -e "api response:\n$api_response"
        continue
    fi

    latest_version=$(echo "$api_response" | grep --color=never tag_name | sed -n 's|.*".*": "\(.*\)".*|\1|p' | sed 's|^v||')
    if [[ -z "$latest_version" ]]; then
        echo "failed to request latest version for $repository!"
        echo -e "api response:\n$api_response"
        continue
    fi
    version=$(grep "Version: " "$file" | cut -d' ' -f2)

    if [[ "$version" != "$latest_version" ]]; then
        echo "$file is not up-to-date ($version -> $latest_version)"

        updated_file=$(cat "$file")
        echo "modifying version in file..."
        updated_file=$(echo "$updated_file" | sed "s|Version: $version|Version: $latest_version|")
        echo "modifying release in file..."
        updated_file=$(echo "$updated_file" | sed "s|Release: [0-9]\+%{?dist}|Release: 1%{?dist}|")
        echo "$updated_file" > "$file"

        echo "running git add && git commit..."
        echo ">>>>>>>>>>"
        git add "$file"
        git commit -m "$repository: $version -> $latest_version"
        echo "<<<<<<<<<<"

        modified=true
        echo "successfully updated $file ($version -> $latest_version)"
    else
        echo "$file is up-to-date ($latest_version)"
    fi
done

if [[ $modified = true ]]; then
    echo "running git push..."
    echo ">>>>>>>>>>"
    git push
    echo "<<<<<<<<<<"
fi
