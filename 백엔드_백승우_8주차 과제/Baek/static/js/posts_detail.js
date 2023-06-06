    const isOwnPost = "{{request.user}}" === "{{post.user}}";

    if (isOwnPost) {
      const postEditBtn = document.getElementById("post_edit");
      const postInput = document.getElementById("post_input");

      postEditBtn.addEventListener("click", () => {
        const isFormVisible = postInput.style.display === "block";

        if (isFormVisible) {
          postInput.style.display = "none";
        } else {
          postInput.style.display = "block";
        }
      });
    }

    function showCommentInput() {
      const commentInput = document.getElementById("comment_input");
      const isFormVisible = commentInput.style.display === "block";

      if (isFormVisible) {
        commentInput.style.display = "none";
      } else {
        commentInput.style.display = "block";
      }
    }

    function showCommentNewInput() {
      const commentEditBtns = document.querySelectorAll(".comment_edit");
      const commentNewInputs = document.querySelectorAll(".comment_new_input");

      commentEditBtns.forEach((btn, index) => {
        btn.addEventListener("click", () => {
          const isFormInvisible = commentNewInputs[index].style.display === "none";

          if (isFormInvisible) {
            commentNewInputs[index].style.display = "block";
          } else {
            commentNewInputs[index].style.display = "none";
          }
        });
      });
    }