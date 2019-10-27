<template>
  <section class="user-profile">
      <user-post-list :userid="userid" />
  </section>
</template>

<script>
import UserPostList from '@/components/UserPostList.vue';

export default {
    data () {
        return {

        }
    },

    props: [
        'userid'
    ],

    components: {
        UserPostList
    }
}
</script>

<style>

</style>