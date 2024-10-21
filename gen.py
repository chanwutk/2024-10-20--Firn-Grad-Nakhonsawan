import os


def page(repo: str, number: int):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Thai Grad 2024: Graduation Photos</title>
<style>
  body {'{'}
    display: flex;
    flex-direction: column;
    align-items: center;
  {'}'}
  .navigation-container {'{'}
    display: flex;
    justify-content: center;
    margin-top: 20px;
  {'}'}
  .p-btn, .n-btn {'{'}
    padding: 10px 20px;
    margin: 0 10px;
    font-size: 16px;
    cursor: pointer;
  {'}'}
  .a-img {'{'}
    width: 30%;
    height: auto;
    margin: 10px;
  {'}'}
</style>
</head>
<body>
  <div class="navigation-container">
    <a href="http://chanwutk.github.io/{repo}/{(number-1):02d}" class="p-btn">prev</a>
    <a href="http://chanwutk.github.io/{repo}/{(number+1):02d}" class="n-btn">next</a>
  </div>
  <div style="display: flex; flex-direction: row; flex-wrap: wrap;">
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}0.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}0.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}1.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}1.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}2.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}2.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}3.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}3.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}4.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}4.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}5.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}5.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}6.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}6.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}7.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}7.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}8.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}8.JPG?raw=true" width=100% height=auto alt=""></a>
    <a class="a-img" href="https://github.com/chanwutk/{repo}/blob/main/DSCF0{number:02d}9.JPG"><img src="https://github.com/chanwutk/{repo}/blob/main/SMALL-DSCF0{number:02d}9.JPG?raw=true" width=100% height=auto alt=""></a>
  </div>
  <div class="navigation-container">
    <a href="http://chanwutk.github.io/{repo}/{(number-1):02d}" class="p-btn">prev</a>
    <a href="http://chanwutk.github.io/{repo}/{(number+1):02d}" class="n-btn">next</a>
  </div>
</body>
</html>
"""

os.makedirs("./docs", exist_ok=True)

first = True
for i in range(25, 38):
    if first:
        with open(f"./docs/index.html", "w") as f:
            f.write(f'<!DOCTYPE html>\n<html><head><meta http-equiv="refresh" content="0;url={i:02d}.html" /></head></html>')

    with open(f"./docs/{i:02d}.html", "w") as f:
        f.write(page('2024-10-20--Firn-Grad-Nakhonsawan', i))
    first = False
