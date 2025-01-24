---
name: "Fix Mayor's Speech Generator"
about: Debug and enhance the speech generator for Codetropolis.
title: "🔧 Fix Mayor's Speech Generator"
labels: ["bug", "enhancement"]
assignees: ""
---

# 🛠️ Fix Mayor's Annual Speech Generator

The mayor’s speech generator is broken! Every time the mayor tries to generate a speech, it either fails or produces garbled output. This is causing frustration and leading to protests in Codetropolis. Your task is to debug and enhance it.

---

## Known Issues

- 📝 Policies are outdated and need refreshing.
- ⚠️ The speech generator sometimes crashes with no clear error.
- 🔄 Policies are being randomly shuffled, creating confusion.

---

## 🗺️ Mission Objectives

1. **Debug the `generate_speech` function**:
   - Ensure it works without errors.
   - Test for edge cases (e.g., empty policy list, malformed data).

2. **Update the `POLICIES` list**:
   - Replace outdated policies with modern priorities for Codetropolis.
   - Example: Focus on sustainability, smart city initiatives, and inclusivity.

3. **Bonus Challenge**:
   - Use the `randomize_policies` function to add a feature where the mayor can shuffle the policies intentionally for fun speeches.

---

## 📂 Files to Work On

- **`policies.py`**: Focus on debugging `generate_speech` and updating `POLICIES`.

---

## 💡 Tips

- Consider adding unit tests to validate the functionality of `generate_speech` and `randomize_policies`.
- Keep in mind user experience—ensure the speech reads smoothly and logically.
- Have fun with creative policy ideas that match Codetropolis's futuristic theme!

---

### Checklist

- [ ] Debugged and fixed `generate_speech`.
- [ ] Updated the `POLICIES` list with modern initiatives.
- [ ] Added functionality to shuffle policies using `randomize_policies`.
- [ ] (Optional) Added unit tests for speech generation and randomization.
- [ ] Tested all changes to ensure smooth functionality.

---

### 🔗 Resources

- [Python String Formatting](https://docs.python.org/3/library/string.html#formatstrings)
- [Exception Handling in Python](https://docs.python.org/3/tutorial/errors.html)

---

Happy coding, and let's get Codetropolis back on track!
