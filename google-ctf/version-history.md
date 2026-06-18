<img width="1352" height="646" alt="Screenshot 2026-06-18 at 9 16 13 AM" src="https://github.com/user-attachments/assets/f0769cdf-7904-4dfe-a669-d76afac08b2c" />

prompt: I wrote some FAQs about this CTF. Took me a few commits to get it right though.
https://version-history-web.2025-bq.ctfcompetition.com/

To solve this, I first tried to inspect, but found nothing much. I also looked at Wayback Machine, and only saw one commit changes in Dec 2025 besides 2026, but no changes. 

I installed git-dumper and got these as results: 
link: https://colab.research.google.com/drive/1OZ7TtQTlnSE2vextVfIcQDeGlYRmGUpF#scrollTo=exBBtzv92hor
in kali: python3 -m venv venv
source venv/bin/activate

> !git-dumper https://version-history-web.2025-bq.ctfcompetition.com/.git ~/website

note to self: add grep 200 | less

here's what I found in one of them: 
https://version-history-web.2025-bq.ctfcompetition.com/.git/logs/HEAD
> 0000000000000000000000000000000000000000 3aa28a2927b56b7c98864107dc7ae4406dd7eb2b Challenge Author <challengeauthor@example.example> 1764186344 +0000	commit (initial): Initial commit
> 3aa28a2927b56b7c98864107dc7ae4406dd7eb2b 42b975b547d9d3fb0494a36b5e60871da13abaf5 Challenge Author <challengeauthor@example.example> 1764186435 +0000	commit: Oops: remove the real flag from the example
>
in kali:
```
> (venv)─(kali㉿kali)-[~/Downloads/git-dumper/web]
└─$ git checkout 3aa28a2927b56b7c98864107dc7ae4406dd7eb2b
Note: switching to '3aa28a2927b56b7c98864107dc7ae4406dd7eb2b'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 3aa28a2 Initial commit
                                                                                                                                                            
┌──(venv)─(kali㉿kali)-[~/Downloads/git-dumper/web]
└─$ ls    
index.html
                                                                                                                                                            
┌──(venv)─(kali㉿kali)-[~/Downloads/git-dumper/web]
└─$ cat index.html 
<!DOCTYPE html>
<html>
<head>
<title>CTF FAQs</title>
<style>
html {
        font-family: Arial, sans-serif;
}
.mono {
        font-family: monospace;
}
.hidden {
        background: black;
        color: black;
}
</style>
</head>
<body>
<h1>CTF FAQs</h1>
<h2>How does it work?</h2>
<p>In summary, we will release several challenges during the CTF, and each challenge has a secret value (a "flag") with the format <span class="mono">CTF{<span class="hidden">y0u_w0uldn_t_d0wnl0ad_a_r3p0</span>}</span>. If you find the flag, you can submit it for points.</p>
<h2>Changelog</h2>
<p>v1.0: initial version.</p>
</body>
</html>
                                                                                                                                                            
┌──(venv)─(kali㉿kali)-[~/Downloads/git-dumper/web]
└─$

```
