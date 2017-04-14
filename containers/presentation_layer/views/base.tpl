<head>
  <title>Word Tools</title>
 </head>
 <body>
  <ul>
   <h2>Word tools running on {{hostname}}</h2>
   <br/>
   <table><tr><td valign="top">
   <table border="1">
    <tr>
     <td align="center">Random word generator</td>
    </tr>
    <tr>
     <td>
      <table>
      <form method="post" action="/random">
        <tr>
         <td>Number</td>
         <td><input type="text" size="2" name="num" value={{random}}></td>
         <td align="right"><input type="submit" value="Generate"></td>
        </tr>
      </form>
      </table>
     </td>
    </tr>
   </table>
   <br/>
   <table border="1">
    <tr>
     <td align="center">Random fixed length</td>
    </tr>
    <tr>
     <td valign="top">
      <table>
      <form method="post" action="/rnd">
        <tr>
         <td>Number</td>
         <td><input type="text" size="2" name="num" value={{rndrows}}></td>
         <td>Length</td>
         <td><input type="text" size="2" name="wordlen" value={{wordlen}}></td>
         <td align="right"><input type="submit" value="Fetch"></td>
        </tr>
      </form>
      </table>
     </td>
    </tr>
   </table>
  </td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td valign="top">
  <table border="1">
   <tr>
    <td align="center">Word finder</td>
   </tr>
   <tr>
    <td>
     <table>
      <form method="post" action="/finder">
       <tr>
        <td>e.g. 'cr_pt_c', 'catas%'.</td>
        <td valign="top"><input type="text" name="partial" size="15" value={{search}}></td>
        <td align="right" valign="top"><input type="submit" name="submit" value="Find"/></td>
       </tr>
      </form>
     </table>
    </td>
   </tr>
 </table>
 <br/>
  <table border="1">
  <tr>
    <td align="center">Password gen</td>
  </tr>
  <tr>
    <td>
    <table>
    <form method="post" action="/pswd">
      <tr>
        <td>Number</td>
        <td><input type="text" size="2" name="num" value={{pswd}}></td>
        <td align="right"><input type="submit" value="Create"></td>
      </tr>
    </form>
    </table>
    </td>
  </tr>
  </table>
 </td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td valign="top">
 <table border="1">
 <tr>
  <td align="left">&nbsp;Anagram solver</td>
 </tr><tr>
  <td>
   <table>
    <form method="post" action="/anagram">
    <tr>
     <td>Anagram</td>
     <td><input type="text" name="anagram" size="15" value={{anagram}}></td>
      <td align="right"><input type="submit" name="submit" value="Solve"/></td>
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
    %for word in output:
        %if word.isalpha():
            <a href="https://en.wiktionary.org/wiki/{{word}}">{{word}}</a><br/>
        %else:
            {{word}}<br/>
        %end
    %end
    </td></tr></table></ul>
%else:
    <br/><br/><br/><br/></br>
    <a href="/test">Presentation layer test</a> - <a href="/apitest">API layer test</a>.
%end
</body>       