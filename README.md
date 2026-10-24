# 별무리 개척단 (GAIA)

초대장으로만 가입하는 우주 개척 커뮤니티 게임이에요. 화면은 GitHub Pages, 로그인·저장은 Firebase(`gaia-d0c35`)를 써요.

## 파일
| 파일 | 하는 일 |
|---|---|
| `index.html` | 게임 본체 (회원가입·로그인 포함) |
| `bgm.mp3` | 배경 음악 |
| `firestore.rules` | Firestore 보안 규칙 → 콘솔 **Firestore Database → 규칙** 탭에 붙여넣고 게시 |
| `storage.rules` | Storage 보안 규칙 → 콘솔 **Storage → 규칙** 탭에 붙여넣고 게시 |

## 처음 설정
1. 이 저장소 **Settings → Pages → Branch: `main` / `/ (root)` → Save**
2. Firebase 콘솔
   - Authentication → 로그인 방법 → **이메일/비밀번호** 사용 설정
   - Authentication → 설정 → **승인된 도메인**에 `gh99mm-dotcom.github.io` 추가
   - Firestore Database 만들기(서울 `asia-northeast3`) → **규칙**에 `firestore.rules` 붙여넣기 → 게시
   - (PAD 이미지) Storage 시작 → **규칙**에 `storage.rules` 붙여넣기 → 게시
3. 사이트가 열리면 **가장 먼저 아이디 `gh99mm`으로 회원가입** (운영자 = 선장, 초대코드 없이 가입)
4. 운영자 창 → **초대장 발급** → 안내문을 친구에게 보내기

게임 주소: https://gh99mm-dotcom.github.io/gaia/
