/*
 * Mock data module.
 */

const module = {
    notifications: [
        { id: 1, title: "New like", text: "Someone liked your post", unread: false },
        { id: 2, title: "Reply", text: "This is a reply", unread: true }
    ]
}

// Export the module if we're in debug mode, an empty object otherwise
export default (function() { if (process.env.NODE_ENV !== 'production') {
    return module;
} else {
    return {};
}})();