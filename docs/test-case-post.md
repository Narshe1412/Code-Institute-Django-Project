# Posts

## Display Posts

1. Separation of Post Types:

   1. Log in with an admin user
   2. Navigate to "All Entries", "Blog" and "News" pages, verify that All Entries contain all the posts from Blog and News and that there are no repeated posts between Blog and News
   3. Verify that posts are ordered by date, showing the most recent the first
   4. Verify that important posts are at the top, and among them, they are also ordered by date.

2. Social buttons:
   1. Navigate to any post.
   2. Click on the Tweet button, verify that a Twitter popup appears and allows you to share the Post URL in your Twitter feed
   3. Click on the Share facebook button, verify that a popup from Facebook appears and allows you to share the Post URL in your Facebook page

## Add Post

1. Create new post:

   1. Log in with an admin or collaborator user, verify that a new "New Post" button appears at the top
   2. Click on "New Post"
   3. Try to submit the empty form and verify that an error message about the required fields appears
   4. Try to submit the form with invalid fields and verify that a relevant error message appears
   5. Try to submit the form with all inputs valid and verify that a success message appears.

2. Post types:
   1. Repeat steps in (1)
   2. Select "News Post" as Post Type and "Is Important" at the bottom, verify that the newly created post is only visible under "News" page
   3. Repeat (1), select "Blog Post" as Post Type, verify that the newly created post is only visible under "Blog" page
   4. Repeat (2, 3), unselecting "Is Important" checkbox at the bottom. Verify that the newly created posts appear below the others marked as Important, and that they don't have the "pin" icon at the top.

## Edit Post

1. Edit active post:
   1. Log in with an admin or collaborator user
   2. Navigate to any post, click "Read More" and then click "Edit Post"
   3. Try to submit the form with invalid fields and verify that a relevant error message appears and the post does not get modified.
   4. Try to submit the form with all inputs valid and verify that a success message appears. Navigate to the post details page and confirm all changes are now recorded.

## Comments

1. Add new comment:

   1. Log in with any user
   2. Navigate to any post, click "Read More" and then scroll to the bottom of the page to the "Comments" section
   3. Try to submit the empty form and verify that an error message about the required fields appears
   4. Try to submit the form with all inputs valid and verify that a success message appears. On refresh, the new posted comment shall appear.

2. Logged user required:
   1. Make sure no user is logged in
      2. Navigate to any post, click "Read More" and then scroll to the bottom of the page to the "Comments" section
      3. Verify no comment can be made due to lack of permissions
