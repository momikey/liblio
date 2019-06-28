/*
 * Later on, this will be a much richer connecting module,
 * probably with Vuex or something. For now, it's all testing.
 */

export function getAllUsers() {
    // Later: API call to the server, fetching all known users;
    // will likely need an API token of some sort.
    return [
        {
            id: 1,
            name: "Test User",
            address: "@test@example.com",
            private: false,
            tags: [
                { key: 'tester', value: 'Tester' },
                { key: 'author', value: 'Author' },
                { key: 'admin', value: 'Administrator' }
            ]
        },
        {
            id: 42,
            name: "Another User",
            address: "@other@example.invalid",
            private: false,
            tags: [
                { key: 'tester', value: 'Tester' },
                { key: 'artist', value: 'Artist' }
            ]
        },
        {
            id: 83,
            name: "Secret Agent",
            address: "@secret@fbi.invalid",
            private: true,
            tags: [
                { key: 'tester', value: 'Tester' }
            ]
        }
    ]
}