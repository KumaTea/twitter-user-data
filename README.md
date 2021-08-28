# Tweet Likes Predict

Predicting likes count of tweets through various factors: a tentative deep learning application

### Purpose

The purpose of this repo is to learn Deep Learning
with [fast.ai](https://docs.fast.ai)'s
[Tabular tutorial](https://docs.fast.ai/tutorial.tabular.html).

#### Update

This project has been suspended: the loss always divergences, and I can't get an acceptable accuracy.

The desensitized data (removing `tid`) will be published on [releases](https://github.com/KumaTea/tweet-likes-predict/releases).

---

## Factors / Parameters

<details>
  <summary>Click to expand...</summary>

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
      <td>yr</td>
      <td>year (UTC+8)</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>2021</td>
    </tr>
    <tr>
      <td>mo</td>
      <td>month (UTC+8)</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>8</td>
    </tr>
    <tr>
      <td>dt</td>
      <td>date (UTC+8)</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>12</td>
    </tr>
    <tr>
      <td>wk</td>
      <td>week (UTC+8)</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>36</td>
    </tr>
    <tr>
      <td>dow</td>
      <td>day of week</td>
      <td>cont</td>
      <td>int</td>
      <td>0 - 6</td>
      <td>2 (Wed)</td>
    </tr>
    <tr>
      <td>doy</td>
      <td>day of year (UTC+8)</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>114</td>
    </tr>
    <tr>
      <td>time</td>
      <td>time (sec of d, UTC+8)</td>
      <td>cont</td>
      <td>int</td>
      <td>0 - 86399</td>
      <td>64800 (18:00)</td>
    </tr>
    <tr>
      <td>last</td>
      <td>interval since last tweet (sec)</td>
      <td>cont</td>
      <td>int</td>
      <td></td>
      <td>114514</td>
    </tr>
    <tr>
      <td>nxt</td>
      <td>interval until next tweet (sec)</td>
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
      <td>crd</td>
      <td>created days</td>
      <td>cont</td>
      <td>str</td>
      <td></td>
      <td>1919</td>
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
3. `foing`, `foer`, `favcnt` and `tcnt` are estimated by `y=x^1.5` based on `crd`

</details>

### Media Types

1. text (No media)
2. pic1
3. pic2
4. pic3
5. pic4
6. gif
7. video
8. ~~poll~~ (can't detect)
9. ~~voice~~ (can't detect)
