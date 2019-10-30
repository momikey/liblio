<template>
    <section class="user-profile">
    <!--
            The user profile "header" contains info about this user.
    -->
        <section class="card user-profile-header">
            <div class="card-image">
                <figure class="image">

                </figure>
            </div>

            <div class="card-content">
                <div class="media">
                    <div class="media-left">
                        <figure class="image is-96x96">

                        </figure>
                    </div>

                    <div class="media-content">
                        <p class="title is-4">{{ currentUser.display_name }}</p>
                        <p class="subtitle is-6">{{ currentUser | formatUser }}</p>

                        <p class="content">{{ currentUser.bio }}</p>
                    </div>
                </div>

                <div class="content">
                    <div class="level">
                        <div class="level-item has-text-centered">
                            <div class="profile-data-column">
                                <p class="heading">{{ labels.posts }}</p>
                                <router-link tag="p" class="title"
                                    :to="{ name: 'user-posts' }"
                                >
                                    {{ currentUserPosts ? currentUserPosts.length : 0 }}
                                </router-link>
                            </div>
                        </div>
                        <div class="level-item has-text-centered">
                            <div class="profile-data-column">
                                <p class="heading">{{ labels.followers }}</p>
                                <router-link tag="p" class="title"
                                    :to="{ name: 'user-followers' }"
                                >
                                    {{ currentUser.followers.length }}
                                </router-link>
                            </div>
                        </div>
                        <div class="level-item has-text-centered">
                            <div class="profile-data-column">
                                <p class="heading">{{ labels.following }}</p>
                                <router-link tag="p" class="title"
                                    :to="{ name: 'user-following' }"
                                >
                                    {{ currentUser.following.length }}
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="card-footer">
                <!-- TODO: Actions (follow, mute, block, etc.) -->
            </div>
        </section>

        <router-view :userid="userid" />
    </section>
</template>

<script>
import { mapGetters } from 'vuex';
import { actorAddress } from '@/modules/uri';

export default {
    data () {
        return {
            labels: {
                posts: "Posts",
                followers: "Followers",
                following: "Following",
            }
        }
    },

    props: [
        'userid'
    ],

    computed: {
        ...mapGetters([
            'currentUser',
            'currentUserPosts'
        ])
    },

    methods: {
        fetch (id) {
            this.$store.dispatch('getUser', id);
            this.$store.dispatch('getUserFollowers', this.userid);
            this.$store.dispatch('getUserFollowing', this.userid); 
        }
    },

    mounted () {
        this.fetch(this.userid);
    },

    filters: {
        formatUser (user) {
            return actorAddress(user.username, user.origin);
        }
    },

    beforeRouteUpdate(to, from, next) {
        this.fetch(to.params.userid);
        next();
    },
}
</script>

<style>
    .user-profile-header {
        margin-top: 1px;
        margin-bottom: 0.5rem;
    }

    .profile-data-column > p.title {
        cursor: pointer;
    }
</style>