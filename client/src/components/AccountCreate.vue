<template>
    <section class="account-create">
        <b-field horizontal :label="labels.username">
            <b-input name="username" expanded
                v-model="account.username"
            />
        </b-field>

        <b-field horizontal :label="labels.name">
            <b-input name="name" expanded
                v-model="account.name"
            />
        </b-field>

        <b-field horizontal :label="labels.role">
            <b-select name="role" :placeholder="labels.rolePlaceholder" expanded
                v-model="account.role"
            >
                <option v-for="role in creatorRoles" :key="role"
                    :value="role"
                >
                    {{ role }}
                </option>
            </b-select>
        </b-field>

        <b-field horizontal :label="labels.bio">
            <b-input type="textarea" rows="5" :placeholder="labels.bioPlaceholder"
                v-model="account.bio"
            />
        </b-field>

        <b-field horizontal :label="labels.tags">
            <b-taginput
                v-model="account.tags"
                :data="availableTags"
                field="value"
            />
        </b-field>

        <b-field horizontal>
            <p class="control">
                <b-button class="is-primary"
                    @click="onCreateAccount"
                >
                    {{ labels.create }}
                </b-button>
            </p>

            <p class="control">
                <b-button
                    @click="onClear"
                >
                    {{ labels.clear }}
                </b-button>
            </p>
        </b-field>
    </section>
</template>

<script>
export default {
    data () {
        return {
            account: {
                username: '',
                name: '',
                role: '',
                bio: '',
                tags: []
            },

            labels: {
                username: "Username",
                name: "Public name",
                role: "Role",
                rolePlaceholder: "What kind of creator are you?",
                bio: "Description",
                bioPlaceholder: "Tell us a little about yourself",
                tags: "Tags",

                create: "Create account",
                clear: "Clear"
            },

            // Some test data to show off the component
            creatorRoles: [
                "Artist",
                "Author",
                "Musician",
                "Photographer"
            ],

            creatorTags: {
                Artist: [
                    { key: 'manga', value: "Manga" },
                    { key: 'painting', value: "Painting" }
                ],

                Author: [
                    { key: 'fantasy', value: "Fantasy" },
                    { key: 'science-fiction', value: "Science Fiction" }
                ],

                Musician: [
                    { key: 'edm', value: "EDM" },
                    { key: 'indie-music', value: "Indie" }
                ],

                Photographer: [
                    { key: 'nature-photo', value: "Nature Photography" },
                    { key: 'portrait', value: "Portraits" }
                ],

                any: [

                ]
            }
        }
    },

    methods: {
        onCreateAccount () {
            console.log("Creating account: ", this.account);
        },

        onClear () {

        }
    },

    computed: {
        availableTags () {
            if (!this.account.role) {
                return []
            } else {
                return this.creatorTags[this.account.role].concat(this.creatorTags["any"]).sort(
                    (a, b) => {
                        if (a.key < b.key) {
                            return -1;
                        } else if (a.key > b.key) {
                            return 1;
                        } else {
                            return 0;
                        }
                    }
                );
            }
        }
    }
}
</script>

<style lang="scss">

</style>
