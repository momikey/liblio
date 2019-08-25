<template>
    <section class="account-create card">
        <form action="" class="card-content" name="account-create" target="_self">
            <p class="subtitle">{{ labels.header }}</p>
            
            <b-field horizontal :label="labels.name">
                <b-input name="name" expanded
                    v-model="profile.name"
                />
            </b-field>

            <b-field horizontal :label="labels.role">
                <b-select name="role" :placeholder="labels.rolePlaceholder" expanded
                    v-model="profile.role"
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
                    v-model="profile.bio"
                />
            </b-field>

            <b-field horizontal :label="labels.tags">
                <b-taginput
                    v-model="profile.tags"
                    :data="filteredTags"
                    autocomplete
                    field="value"
                    :placeholder="labels.tagsPlaceholder"
                    @typing="getFilteredTags"
                />
            </b-field>

            <b-field class="level">
                <div class="level-item">
                    <b-button class="is-primary create-account-button"
                        @click="onNext"
                    >
                        {{ labels.next }}
                    </b-button>
                    <b-button class="create-account-button"
                        @click="onBack"
                    >
                        {{ labels.back }}
                    </b-button>
                </div>
            </b-field>
        </form>
    </section>
</template>

<script>
export default {
    data () {
        return {
            profile: {
                name: '',
                role: '',
                bio: '',
                tags: []
            },

            labels: {
                name: "Public name",
                role: "Role",
                rolePlaceholder: "What kind of creator are you?",
                bio: "Description",
                bioPlaceholder: "Tell us a little about yourself",
                tags: "Tags",
                tagsPlaceholder: "Add some tags to help others find your work",

                next: "Next",
                back: "Back",

                header: "Start your profile"
            },

            // Placeholder data: this will be filled in by the server soon

            // Backing field for filtered tags list
            filteredTags: [],

            // Some test data to show off the component
            creatorRoles: [
                "Artist",
                "Author",
                "Musician",
                "Photographer"
            ],

            // Some example tags
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
                    { key: 'bot', value: "Bot" }
                ]
            }
        }
    },

    computed: {
        availableTags () {
            if (!this.profile.role) {
                return this.creatorTags["any"];
            } else {
                return this.creatorTags[this.profile.role].concat(this.creatorTags["any"]).sort(
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
    },

    methods: {
        onNext () {
            this.$emit('next-step', this.profile);
        },

        onBack () {
            this.$emit('previous-step');
        },

        getFilteredTags (text) {
            this.filteredTags = this.availableTags.filter(tag => 
                tag.value.toLowerCase().startsWith(text.toLowerCase())
            );
        }
    },

    mounted () {
        this.filteredTags = this.availableTags;
    }
}
</script>
