#!/bin/bash

for file in $(find . -type f -name "*.spec"); do
	version=$(cat $file | grep "Version: " | cut -d' ' -f2)

	url=$(cat $file | grep "URL: " | cut -d' ' -f2)
	repository=$(echo $url | sed -n 's|.*github.com/\(.*\)$|\1|p')
	api_response=$(curl -s "https://api.github.com/repos/$repository/releases/latest")
	if [[ $? -ne 0 ]]; then
		echo failed to request latest version for $repository!
		continue
	fi
	latest_version=$(echo "$api_response" | grep --color=never tag_name | sed -n 's|.*".*": "\(.*\)".*|\1|p' | sed 's|^v||')

	if [[ "$version" != "$latest_version" ]]; then
		echo "$file is not up-to-date ($version -> $latest_version)"

		updated_file=$(cat $file | sed "s|Version: $version|Version: $latest_version|")
		echo "$updated_file" > $file
	
		echo "running git add && git commit"
		git add $file
		git commit -m "Update $repository"

		echo "successfully updated $file from $version to $latest_version!"
	else
		echo "$file is up-to-date ($version)"
	fi
done

echo "running git push..."
git push
