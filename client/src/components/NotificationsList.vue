<template>
    <section class="notifications-list">
        <b-message :title="labels.title" :closable="false"
            type="is-primary" :active="active"
        >
            <div v-for="note in notifications" :key="note.id"
                class="card"
            >
                <div class="card-header">
                    <p class="card-header-title">
                        {{ note.title }}
                    </p>
                </div>

                <div class="card-content">
                    {{ note.text }}
                </div>
            </div>
        </b-message>

        <footer>
            <router-link to="/user/notifications">
                {{ labels.all }}
            </router-link>
        </footer>
    </section>
</template>

<script>
export default {
    data () {
        return {
            labels: {
                title: "Notifications",
                all: "All notifications"
            }
        }
    },

    props: [
        'active',
        'notifications'
    ]
}
</script>

<style lang="scss">

</style>
