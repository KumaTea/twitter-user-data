# Tweet Likes Predict

Predicting likes count of tweets through various factors: a tentative deep learning application

### Purpose

The purpose of this repo is to learn Deep Learning
with [fast.ai](https://docs.fast.ai)'s
[Tabular tutorial](https://docs.fast.ai/tutorial.tabular.html).

---

## Factors / Parameters

<table>
  <thead align="center">
    <tr>
      <th>Name</th>
      <th>Meaning</th>
      <th>Type</th>
      <th>Data Type</th>
      <th>Range</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody align="center">
    <tr>
      <td colspan=6><b>Tweet</b></td>
    </tr>
    <tr>
      <td>tid</td>
      <td>tweet id</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>11451419198101919810</td>
    </tr>
    <tr>
      <td>doy</td>
      <td>day of year (UTC)</td>
      <td>cont</td>
      <td>int</td>
      <td>1 - 366</td>
      <td>114 (April 24)</td>
    </tr>
    <tr>
      <td>dow</td>
      <td>day of week</td>
      <td>cat</td>
      <td>int</td>
      <td>1 - 7</td>
      <td>3 (Wed)</td>
    </tr>
    <tr>
      <td>time</td>
      <td>time (sec of d, UTC)</td>
      <td>cont</td>
      <td>int</td>
      <td>0 - 86399</td>
      <td>64800 (18:00)</td>
    </tr>
    <tr>
      <td>intv</td>
      <td>interval since last tweet (sec)</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>114514</td>
    </tr>
    <tr>
      <td>tlen</td>
      <td>tweet length</td>
      <td>cont</td>
      <td>int</td>
      <td>0 - 140</td>
      <td>114</td>
    </tr>
    <tr>
      <td>media</td>
      <td>media</td>
      <td>cat</td>
      <td>str</td>
      <td>(see details)</td>
      <td>'Empty'</td>
    </tr>
    <tr>
      <td>src</td>
      <td>source</td>
      <td>cat</td>
      <td>str</td>
      <td></td>
      <td>'Twitter for Android'</td>
    </tr>
    <tr>
      <td>isq</td>
      <td>is quoted status</td>
      <td>cat</td>
      <td>int</td>
      <td>0, 1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>sen</td>
      <td>possibly sensitive</td>
      <td>cat</td>
      <td>int</td>
      <td>0, 1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>lang</td>
      <td>language</td>
      <td>cat</td>
      <td>str</td>
      <td></td>
      <td>'zh'</td>
    </tr>
    <tr>
      <td colspan=6><b>User</b></td>
    </tr>
    <tr>
      <td>snlen</td>
      <td>screen_name length</td>
      <td>cont</td>
      <td>int</td>
      <td>1 - 15</td>
      <td>8 (i.e. KumaTea0)</td>
    </tr>
    <tr>
      <td>prot</td>
      <td>protected</td>
      <td>cat</td>
      <td>int</td>
      <td>0, 1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>foing</td>
      <td>friends_count</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>114</td>
    </tr>
    <tr>
      <td>foer</td>
      <td>followers_count</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>514</td>
    </tr>
    <tr>
      <td>cry</td>
      <td>created_at year</td>
      <td>cat</td>
      <td>str</td>
      <td>2006 -</td>
      <td>2015</td>
    </tr>
    <tr>
      <td>favcnt</td>
      <td>favourites_count</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>114514</td>
    </tr>
    <tr>
      <td>tcnt</td>
      <td>statuses_count</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>114514</td>
    </tr>
    <tr>
      <td colspan=6><b>Misc</b></td>
    </tr>
    <tr>
      <td colspan=6><b>y</b></td>
    </tr>
    <tr>
      <td>lcnt</td>
      <td>likes count</td>
      <td>cont</td>
      <td>int</td>
      <td>/</td>
      <td>114</td>
    </tr>
  </tbody>
</table>

Note:

1. `cont` = continuous, `cat` = categorical
2. all ``int`` value will be converted to `float` for faster computing (idk why)
3. `foing`, `foer`, `favcnt` and `tcnt` are estimated by `y=x^1.5` based on `cry`

### Media Types

1. None
2. 1 pic
3. 2 pic
4. 3 pic
5. 4 pic
6. gif
7. video
8. voice
9. poll
