
$ git config --global user.name "kingleoric2010"

dell@DESKTOP-QTR5CTS MINGW64 /d/myproject/chongshi/guest (master)
$ git config --global user.email "kingleoric2010@163.com"
$ ssh-keygen -t rsa -C "kingleoric2010@163.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/dell/.ssh/id_rsa):
Created directory '/c/Users/dell/.ssh'.

$ git init
$ git add guest/
$ git commit -m "third"
$ git remote add origin https://github.com/kingleoric2010/chongshi.git
$ git push -u origin master
Counting objects: 34, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (32/32), done.
Writing objects: 100% (34/34), 15.76 KiB | 0 bytes/s, done.
Total 34 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/kingleoric2010/chongshi.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.


