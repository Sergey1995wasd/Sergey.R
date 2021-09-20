<html>
<head>
<title>6_3.py</title>
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
6_3.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">json </span><span class="s0">import </span><span class="s1">dump</span>
<span class="s0">from </span><span class="s1">itertools </span><span class="s0">import </span><span class="s1">zip_longest</span>


<span class="s0">with </span><span class="s1">open(</span><span class="s2">'users.csv'</span><span class="s0">, </span><span class="s2">'r'</span><span class="s0">, </span><span class="s1">encoding=</span><span class="s2">'utf-8'</span><span class="s1">) </span><span class="s0">as </span><span class="s1">users:</span>
    <span class="s0">with </span><span class="s1">open(</span><span class="s2">'hobby.csv'</span><span class="s0">, </span><span class="s2">'r'</span><span class="s0">, </span><span class="s1">encoding=</span><span class="s2">'utf-8'</span><span class="s1">) </span><span class="s0">as </span><span class="s1">hobby:</span>

        <span class="s0">if </span><span class="s1">len(users.readlines()) &gt;= len(hobby.readlines()):</span>
            <span class="s1">users.seek(</span><span class="s3">0</span><span class="s1">)</span>
            <span class="s1">hobby.seek(</span><span class="s3">0</span><span class="s1">)</span>
            <span class="s0">with </span><span class="s1">open(</span><span class="s2">'dict_n_h.json'</span><span class="s0">, </span><span class="s2">'w'</span><span class="s0">, </span><span class="s1">encoding=</span><span class="s2">'utf-8'</span><span class="s1">) </span><span class="s0">as </span><span class="s1">f:</span>
                <span class="s1">all_list = zip_longest((</span><span class="s2">' '</span><span class="s1">.join(us.split(</span><span class="s2">','</span><span class="s1">)) </span><span class="s0">for </span><span class="s1">us </span><span class="s0">in </span><span class="s1">users)</span><span class="s0">, </span><span class="s1">hobby)</span>
                <span class="s1">my_dict = {str(el[</span><span class="s3">0</span><span class="s1">]).strip():str(el[</span><span class="s3">1</span><span class="s1">].strip)} </span><span class="s0">for </span><span class="s1">el </span><span class="s0">in </span><span class="s1">all_list}</span>

                <span class="s1">dump(my_dict</span><span class="s0">, </span><span class="s1">f </span><span class="s0">, </span><span class="s1">ensure_ascii=</span><span class="s0">False, </span><span class="s1">indent=</span><span class="s3">4</span><span class="s1">))</span>
            <span class="s1">print (my_dict)</span>
        <span class="s0">else</span><span class="s1">:</span>
             <span class="s1">exit(</span><span class="s3">1</span><span class="s1">)</span>

</pre>
</body>
</html>