---
name: "Fix Duplicate Newsfeed"
about: Debug and fix the duplicate newsfeed issue in Codetropolis.
title: "🔧 Fix Duplicate Newsfeed"
labels: ["bug"]
assignees: ""
---

# 🛠️ Fix Duplicate Newsfeed in Codetropolis

Codetropolis’ newsfeed is malfunctioning! News stories are being duplicated in the list, causing confusion for citizens. Your mission is to fix the issue and ensure the newsfeed returns unique stories.

---

## Known Issue

- 🔄 **Duplicate News**: News stories are being duplicated in the `fetch_news` function, causing multiple identical entries to appear.

---

## 🗺️ Mission Objectives

1. **Fix the Duplicate News**:
   - Identify and resolve the bug in the `fetch_news` function.
   - Ensure that each news story appears only once in the feed.

---

## 📂 Files to Work On

- **`newsfeed.py`**: Focus on debugging the `fetch_news` function to remove duplicate entries.

---

## 💡 Tips

- Carefully examine the logic in the `fetch_news` function, and check if there's any intentional duplication of news.
- Test the newsfeed to ensure no duplicates appear after your fix.

---

### Checklist

- [ ] Identified and fixed the bug causing duplicate news entries.
- [ ] Tested the newsfeed to ensure all stories are unique.
- [ ] (Optional) Added comments to clarify code logic.

---

### 🔗 Resources

- [Python List Handling](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

---

Happy coding, and let's clean up Codetropolis' newsfeed for the citizens!
