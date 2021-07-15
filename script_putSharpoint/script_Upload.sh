#!/bin/bash

access_token=$(curl --location -vvv --request POST 'https://accounts.accesscontrol.windows.net/c0912129-feb8-4169-b3ec-785103c61b93/tokens/OAuth/2'  --form 'grant_type=client_credentials' -F 'client_id=c6ceb672-2535-474b-9d92-f0d01de950af@c0912129-feb8-4169-b3ec-785103c61b93' -F 'client_secret=VaYuYLndaehtMywfVgvNOhTiIuvx8GHSkZT2s2z4BkI=' -F 'resource=00000003-0000-0ff1-ce00-000000000000/hexaboxcloud.sharepoint.com@c0912129-feb8-4169-b3ec-785103c61b93' | jq -r '.access_token' )

curl --location -vvv --request POST "http://hexaboxcloud.sharepoint.com/_api/web/GetFolderByServerRelativePath(DecodedUrl=@a1)/Files/AddUsingPath(DecodedUrl=@a2,AutoCheckoutOnInvalidData=@a3)?access_token=$access_token&@a1=%27%2FShared%20Documents%27&@a2=%27jerome%2jeroml%2Ecsv%27&@a3=true" --header 'Accept: application/json;odata=verbose' --header 'Content-Length: 0'


