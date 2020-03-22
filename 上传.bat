
SET GenFile=./.git

if not exist %GenFile% (
	git init
)

git add .
git commit -m 'upload'
git remote rm origin
git remote add origin https://github.com/xingchencxkj/starx.git
git push origin master
