name: 📰 Debug Newsfeed
description: Fix the duplicate news entries and add pagination.
title: "📰 Fix Newsfeed Issues"
labels: bug, help wanted
body:
  - type: markdown
    attributes:
      value: |
        ### Debug the Codetropolis Newsfeed System

        The newsfeed system is duplicating stories and doesn't support pagination. Citizens are getting annoyed seeing the same stories multiple times.

        ---
  - type: textarea
    attributes:
      label: What bug did you encounter?
      description: Provide details about the duplicate stories or pagination issues.
      placeholder: "Example: Duplicate stories appear because of ..."
  - type: textarea
    attributes:
      label: How do you plan to fix it?
      description: Outline your steps to resolve the issues.
      placeholder: "Example: Update the `fetch_news` function to remove duplicates..."
