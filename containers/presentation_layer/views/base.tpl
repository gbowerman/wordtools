<head>
  <title>Word Tools</title>
 </head>
 <body>
  <ul>
   <h2>Word tools running on {{hostname}}</h2>
   <br/>
   <table><tr><td>
   <table border="1">
    <tr>
     <td align="center">Random Word Generator</td>
    </tr>
    <tr>
     <td>
      <table>
      <form method="post" action="/random">
        <tr>
         <td>Number</td>
         <td><input type="text" size="2" name="num" value=10></td>
         <td align="right"><input type="submit" value="Generate"></td>
        </tr>
      </form>
      </table>
     </td>
    </tr>
   </table>
  </td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td valign="top">
  <table border="1">
   <tr>
   </tr>
   <tr>
    <td>
     <table>
      <form method="post" action="/finder">
       <tr>
        <td>e.g. 'cr_pt_c', 'cat%'.</td>
        <td valign="top"><input type="text" name="partial" size="20" value=am_s_ng></td>
        <td align="right" valign="top"><input type="submit" name="submit" value="Find"></td>
       </tr>
      </form>
     </table>
    </td>
   </tr>
 </table>
 </td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td valign="top">
 <table border="1">
 <tr>
  <td align="left">&nbsp;Anagram Solver</td>
 </tr><tr>
  <td>
   <table>
    <form method="post" action="/anagram">
    <tr>
     <td>Anagram</td>
     <td><input type="text" name="anagram" size="20" value=listen></td>
      <td align="right"><input type="submit" name="submit" value="Solve"></td>
     </tr>
     </form>
    </table>
   </td>
  </tr>
 </table>
</tr></tr></table>
%if output is not None:
    <br/><br/>
    <table border="1"><tr><th>Word(s)</th></tr><tr><td>
    {{output}}
    </td></tr></table></ul>
%end
</body>       