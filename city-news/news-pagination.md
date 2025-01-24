---

# Fix the Duplicate Newsfeed Issue and Paginate Stories

The Codetropolis newsfeed has a bug: it’s showing duplicate stories and needs pagination to make browsing easier for citizens. Help us fix the issues and make the news more manageable!

---

## Known Issues
1. **Duplicate news stories**: The same news story is appearing multiple times.
2. **No pagination**: The newsfeed is overwhelming citizens with all the news at once, without any way to navigate through older or newer stories.
3. **Inefficient loading**: All news stories are loaded at once, leading to slow loading times.

---

## Your Mission
1. **Fix the duplicate news stories**: Debug the `fetchNews()` function or API to prevent duplicate news items from appearing in the feed.
2. **Add pagination**: Modify the frontend to show only a limited number of news stories per page and add pagination controls like "Next" and "Previous."
3. **Optimize the newsfeed**: Improve the performance by only loading and displaying a manageable number of news stories at a time.

---

### Bonus Challenge
- **Dynamic news**: Add a feature where users can filter the news by categories (e.g., "Local," "World," "Technology") and see only the relevant news.

---