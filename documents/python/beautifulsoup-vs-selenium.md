# BeautifulSoup VS Selenium


## BeautifulSoup
- html 정보 파싱
- 서버에서 HTML을 다운 받기 때문에 서버사이드 렌더링을 사용하지 않는 SPA 사이트나, javascipt 렌더링을 필요로 하는 사이트들은 크롤링하기 까다롭다.

## Selenium
- 웹 동작
- 웹 페이지에서 javascript 렌더링을 통해 생성되는 데이터들을 손쉽게 가져올 수 있다. 즉 사용자의 행동을 동적으로 추가할 수 있다.
- 웹 브라우저를 실제로 진행시키는 방법이기 때문에 속도도 많이 느리고, 메모리도 상대적으로 많이 차지한다.