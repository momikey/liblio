<template>
    <section class="profile-editor" v-if="profile_">
        <b-field horizontal :label="labels.name">
            <b-input v-model="profile_.name">
            </b-input>
        </b-field>

        <b-field horizontal :label="labels.bio">
            <b-input type="textarea" v-model="profile_.bio">

            </b-input>
        </b-field>

        <div class="avatar-container">
            <b-field :label="labels.avatar">
                <!-- TODO: Avatar upload/display -->
                <b-upload v-model="avatarFile" accept="image/*">
                    <a class="button is-primary">
                        <b-icon icon="upload" />
                        <span>{{ labels.upload }}</span>
                    </a>
                </b-upload>
            </b-field>

            <figure class="image is-128x128 creator-avatar-figure">
                <!-- <img class="is-rounded" :src="localImage" v-if="localImage" />
                <img class="is-rounded" :src="profile_.avatar" v-else-if="profile_.avatar" />
                -->
                <img class="is-rounded" :src="thumbnail" v-if="thumbnail" />
                <img class="is-rounded" src="../assets/logo.png" v-else />
            </figure>
        </div>

        <br />

        <b-field grouped position="is-centered" class="profile-editor-controls">
            <b-button class="button control is-primary" @click="onSave">
                {{ labels.save }}
            </b-button>
            <b-button class="button control" @click="onCancel">
                {{ labels.cancel}}
            </b-button>
        </b-field>
    </section>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    data () {
        return {
            // Can't call this `_profile` because of dumb Vue restrictions
            profile_: {
                name: '',
                bio: '',
                avatar: '',
                settings: {},
            },

            avatarFile: undefined,
            localImage: '',

            labels: {
                name: "Your name",
                bio: "Bio",
                avatar: "Avatar",

                upload: "Click to upload a new avatar",
                save: "Save changes",
                cancel: "Cancel"
            }
        }
    },

    computed: {
        ...mapGetters({
            'profile': 'myProfile'
        }),

        thumbnail () {
            return this.localImage || this.profile_.avatar || false;
        }
    },

    methods: {
        onSave () {
            this.$store.dispatch('updateProfile', {
                newProfile: this.profile_,
                avatarFile: this.avatarFile
            });
        },

        onCancel () {
            // TODO: Warning if the user has changed something?
            // Note that deps have already pulled in deep-equal
            this.$router.back();
        }
    },

    watch: {
        avatarFile () {
            console.log(this.avatarFile);

            const reader = new FileReader();
            
            reader.onload = function () {
                this.localImage = reader.result;
                console.log(this.localImage);
            };

            reader.readAsDataURL(this.avatarFile);
        }
    },

    mounted () {
        this.profile_ = {...this.profile};
    }
}
</script>

<style>
    .avatar-container > figure{
        margin: 0 auto;
        padding-top: 0.5rem;
    }

    .profile-editor-controls {
        margin-top: 3rem;
    }
</style>