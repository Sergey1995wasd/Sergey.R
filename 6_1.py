<html>
<head>
<title>6_1.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
.s3 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
6_1.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">lib2to3.pgen2.grammar </span><span class="s0">import </span><span class="s1">line</span>

<span class="s0">with </span><span class="s1">open(</span><span class="s2">'nginx_logs.txt'</span><span class="s0">, </span><span class="s2">'r'</span><span class="s0">, </span><span class="s1">encoding=</span><span class="s2">'utf8'</span><span class="s1">) </span><span class="s0">as </span><span class="s1">f:</span>
    <span class="s1">content = ((line.split()[</span><span class="s3">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">line.split()[</span><span class="s3">5</span><span class="s1">][</span><span class="s3">1</span><span class="s1">:]</span><span class="s0">, </span><span class="s1">line.split()[</span><span class="s3">6</span><span class="s1">]) </span><span class="s0">for </span><span class="s1">line </span><span class="s0">in </span><span class="s1">f)</span>
    <span class="s0">for </span><span class="s1">i </span><span class="s0">in  </span><span class="s1">content:</span>
        <span class="s1">print(i)</span>

</pre>
</body>
</html>