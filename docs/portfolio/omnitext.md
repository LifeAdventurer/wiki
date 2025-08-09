# OmniText

!!! success "Accessibility App"
    A zero-build, client-side phrase board app built with plain HTML, CSS, and JavaScript.

## Website

!!! link "Live Application"
    Try OmniText at [https://lifeadventurer.github.io/OmniText/](https://lifeadventurer.github.io/OmniText/)

## Overview

Designed for people who have difficulty speaking (e.g., when they are sick), OmniText
allows you to save your favorite words or sentences and display them instantly in
full screen for quick and easy communication.

!!! important "Privacy First"
    **All your data stays on your device!** OmniText uses browser localStorage,
    meaning your phrases are stored locally and never sent to any server. Your
    privacy is guaranteed.

## Features

!!! tip "Key Features"
    - **Zero Build Process**: No complex build tools or frameworks needed. Just
      plain HTML, CSS (via Tailwind CDN and inline styles), and JavaScript.
    - **100% Client-Side**: Runs entirely in the user's browser with no server
      dependencies.
    - **Complete Privacy**: All data stored locally in your browser's
      `localStorage` - nothing is ever sent to external servers.
    - **Full-Screen Display**: Tap a saved phrase to display it prominently in
      full screen, making it easy for others to read.
    - **Optional Sorting by Usage:** Enable or disable sorting phrases based on how
      frequently they are used.
    - **Optional Usage Display:** Show or hide the usage count for each phrase.
    - **Progressive Web App (PWA)**:
        - **Installable**: Add OmniText to your device's home screen for quick
          access, just like a native app.
        - **Offline Support**: Thanks to the Service Worker, the core
          application assets are cached, allowing you to access and use your
          saved phrases even without an internet connection.
    - **Responsive Design**: Adapts to various screen sizes, from mobile phones
      to desktops.

## Technology Stack

- **Frontend**: Plain HTML, CSS, JavaScript
- **Styling**: Tailwind CSS (via CDN) and inline styles
- **Storage**: Browser localStorage (100% client-side)
- **PWA Features**: Service Worker for offline support
- **Deployment**: Static hosting on GitHub Pages

## How to Use

!!! example "Step-by-Step Guide"
    1. **Enter a phrase** or sentence into the text input field.
    2. **Click "Add Text"** or press Enter to save the phrase.
    3. **Saved phrases appear** below as buttons.
    4. **Click any saved phrase button** to display it in full screen.
    5. **Tap anywhere** on the full-screen display to dismiss it.
    6. **Click the "✕" button** next to a phrase to delete it (requires confirmation).
    7. Click the "Clear All Phrases" button to remove all saved phrases (requires
       confirmation).
    8. Toggle **Sort by usage** to order phrases by frequency instead of insertion
       order.
    9. Toggle **Show usage** to display or hide the usage count badges.

## Use Cases

!!! example "Perfect For"
    - People with temporary speech difficulties
    - Healthcare communication
    - Accessibility support
    - Emergency communication
    - Language learning and practice
    - Situations requiring quick, clear communication

## Project Goals

The primary goal of OmniText is to provide a simple, reliable, and Accessibility
communication tool that requires no technical setup or internet connection once
loaded. It's designed to be immediately usable by anyone who needs to communicate
through text display.

!!! success "Privacy & Security"
    - **No Server Required**: Everything runs in your browser
    - **No Data Collection**: Your phrases never leave your device
    - **No Tracking**: No analytics or user tracking
    - **Complete Control**: You own and control all your data

## Development Philosophy

- **Simplicity**: No complex frameworks or dependencies
- **Accessibility**: Designed with universal access in mind
- **Reliability**: Works offline and across different browsers
- **Ease of Use**: Intuitive interface requiring minimal learning
- **Privacy**: All data stays local to your device - no external dependencies
- **Performance**: Fast loading and responsive interactions
