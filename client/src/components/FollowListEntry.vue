<template>
    <div class="media">
        <figure class="media-left image is-64x64">
            <img v-if="user.avatar" :src="user.avatar" :alt="user.display_name" />
        </figure>
        <div class="media-content">
            <p class="is-title is-6">
                {{ user.display_name }}
            </p>
            <p class="is-7">
                <router-link :to="userAddress()" class="has-text-main">
                    {{ user | format }}
                </router-link>
            </p>
        </div>
    </div>
</template>

<script>
import { actorAddress } from "@/modules/uri";

export default {
    data () {
        return {

        }
    },

    props: [
        'user'
    ],

    methods: {
        userAddress () {
            return `/web/user/${this.user.id}`;
        }
    },

    filters: {
        format (user) {
            return actorAddress(user.username, user.origin);
        }
    }
}
</script>