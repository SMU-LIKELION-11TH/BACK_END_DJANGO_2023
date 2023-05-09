# [과제 #1] 게시판 ERD 모델링하기

## 게시판 데이터 모델링

![](게시판_ERD_김동주.png)

```mermaid
erDiagram
    User ||--o{ Post : "creates"
    User ||--o{ Comment : "creates"
    User ||--o{ Reply : "creates"

    Post ||--o{ Comment : "contains"
    Comment ||--o{ Reply : "contains"

    User {
        INTEGER id PK "사용자 고유 식별자"
        STRING username "사용자명"
        STRING password "비밀번호"
    }

    Post {
        INTEGER id PK "게시글 고유 식별자"
        INTEGER author FK "작성자. = User.id"
        STRING content "게시글댓ㄱ 내용"
    }

    Comment {
        INTEGER id PK "댓글 고유 식별자"
        INTEGER author FK "작성자. = User.id"
        INTEGER post FK "댓글이 달린 포스트. = Post.id"
        STRING content "댓글 내용"
    }

    Reply {
        INTEGER id PK "답글 고유 식별자"
        INTEGER author FK "작성자. = User.id"
        INTEGER comment FK "답글이 달린 댓글. = Comment.id"
        STRING content "답글 내용"
    }
```
