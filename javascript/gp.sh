#!/bin/sh

function addcommitpush () {

current=$(git branch | grep "*" | cut -b 3-)

message=\'"$@"\'
git add . && git commit -a -m "JavaScript lesson Commits"

echo "Where to push?"
read -i "$current" -e branch

echo "You sure you wanna push? (y/n)"
read -i "y" -e yn

if [ "$yn" = y ]; then
 # git push origin "$branch"
  git push git@github.com:cmukoyi/learn_2022_wsl.git
else
  echo "Retry"
fi

}

addcommitpush $1
