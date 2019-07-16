#!/usr/bin/env bash
git add --all
git commit -m "$(date) update"
git push
ssh root@ssh.aiops.org "mkdir -p /srv/workshop.aiops.org"
echo "begin copy"
scp -r $(realpath .) root@ssh.aiops.org:/srv/workshop.aiops.org