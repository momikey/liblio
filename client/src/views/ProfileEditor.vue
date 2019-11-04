<template>
    <section class="profile-editor">
        <b-field horizontal :label="labels.name">
            <b-input v-model="name">
            </b-input>
        </b-field>

        <b-field horizontal :label="labels.bio">
            <b-input type="textarea" v-model="bio">

            </b-input>
        </b-field>

        <div class="avatar-container">
            <b-field :label="labels.avatar">
                <!-- TODO: Avatar upload/display -->
                <b-upload v-model="avatarFile">
                    <a class="button is-primary">
                        <b-icon icon="upload" />
                        <span>{{ labels.upload }}</span>
                    </a>
                </b-upload>
            </b-field>

            <figure class="image is-128x128 creator-avatar-figure">
                <img class="is-rounded" :src="avatar" v-if="avatar"/>
                <img class="is-rounded" src="../assets/logo.png" v-else />
            </figure>
        </div>
    </section>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    data () {
        return {
            name: '',
            bio: '',
            avatar: '',
            settings: {},

            avatarFile: null,

            labels: {
                name: "Your name",
                bio: "Bio",
                avatar: "Avatar",

                upload: "Click to upload a new avatar",
            }
        }
    },

    computed: {
        ...mapGetters({
            'profile': 'myProfile'
        })
    },

    mounted () {
        console.log(this.profile.display_name);
        this.name = this.profile.display_name;
        this.bio = this.profile.bio;
        this.avatar = this.profile.avatar;
        this.settings = this.profile.settings;
    }
}
</script>

<style>
    .avatar-container > figure{
        margin: 0 auto;
        padding-top: 0.5rem;
    }
</style>