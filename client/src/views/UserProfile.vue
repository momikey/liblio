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
                                <p class="title" @click="showPosts">
                                    {{ currentUserPosts ? currentUserPosts.length : 0 }}
                                </p>
                            </div>
                        </div>
                        <div class="level-item has-text-centered">
                            <div class="profile-data-column">
                                <p class="heading">{{ labels.followers }}</p>
                                <p class="title" @click="showFollowers">
                                    {{ currentUser.followers.length }}
                                </p>
                            </div>
                        </div>
                        <div class="level-item has-text-centered">
                            <div class="profile-data-column">
                                <p class="heading">{{ labels.following }}</p>
                                <p class="title" @click="showFollowing">
                                    {{ currentUser.following.length }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="card-footer">
                <!-- TODO: Actions (follow, mute, block, etc.) -->
            </div>
        </section>

        <component :is="showPage" :userid="userid" :key="userid" />
    </section>
</template>

<script>
import UserPostList from '@/components/UserPostList.vue';
import UserFollowersList from '@/components/UserFollowersList.vue';
import UserFollowingList from '@/components/UserFollowingList.vue';
import { mapGetters } from 'vuex';
import { actorAddress } from '@/modules/uri';

export default {
    data () {
        return {
            showPage: 'user-post-list',

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

    components: {
        UserPostList,
        UserFollowersList,
        UserFollowingList
    },

    methods: {
        showPosts () {
            this.showPage = 'user-post-list';
        },

        showFollowers () {
            this.showPage = 'user-followers-list';
        },

        showFollowing () {
            this.showPage = 'user-following-list';
        },

        fetch (id) {
            this.$store.dispatch('getUser', id);
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