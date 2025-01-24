---
name: "Mission 2a: Implement Pagination for Newsfeed"
about: Add pagination to Codetropolis' newsfeed so users can browse news in pages.
title: "🔧 Implement Pagination for Newsfeed"
labels: ["bug", "enhancement"]
assignees: ""
---


# 🛠️ Implement Pagination for Newsfeed in Codetropolis

The Codetropolis newsfeed needs pagination! Currently, all news stories are displayed at once, which is overwhelming. Your mission is to implement pagination so users can easily navigate through news stories.

---

## Known Issues

- 📄 **No Pagination**: The current newsfeed shows all news stories at once, making it hard to browse.

---

## 🗺️ Mission Objectives

1. **Add Pagination Logic to the Backend**:
   - Implement pagination in the `/api/news` API route to return a subset of news stories (e.g., 5 per page).
   - Use query parameters such as `page` and `per_page` to determine which stories to show.

2. **Update the Frontend to Handle Pagination**:
   - Modify the frontend JavaScript to fetch paginated data and display the appropriate page of news stories.
   - Add controls (e.g., "Next" and "Previous" buttons) for users to navigate between pages.

---

## 📂 Files to Work On

- **`api.py`**: Implement pagination logic for the news API route.
- **Frontend (HTML/JS)**: Update the frontend to handle and display paginated news stories.

---

## 💡 Tips

- Consider using query parameters like `?page=1&per_page=5` to control pagination.
- Update the frontend to display buttons that allow users to move between pages (e.g., "Next" and "Previous").
- Make sure the pagination works smoothly and doesn't break the newsfeed display.

---

### Checklist

- [ ] Implemented pagination in the backend API.
- [ ] Updated the frontend to display paginated news.
- [ ] Added "Next" and "Previous" buttons for navigation.
- [ ] Tested the pagination functionality to ensure smooth user experience.

---

### 🔗 Resources

- [Flask Pagination](https://flask.palletsprojects.com/en/2.0.x/patterns/pagination/)
- [Frontend Pagination Techniques](https://www.smashingmagazine.com/2014/09/infinite-scrolling-vs-pagination/)

---

Happy coding, and let’s make the Codetropolis newsfeed more user-friendly! 

---

This version cleans up a bit of the formatting and makes sure all information is consistent. Let me know if you need further adjustments!
