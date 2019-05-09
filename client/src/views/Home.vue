<template>
  <div class="home columns">
    <div class="column is-two-thirds">
      <img alt="Vue logo" src="../assets/logo.png">
      <p>We'll put posts and things like that over here</p>
    </div>

    <div class="column is-one-third">
      <creator-panel />
    </div>
  </div>
</template>

<script>
import CreatorPanel from '@/components/CreatorPanel.vue'

export default {
  name: 'home',
  components: {
    CreatorPanel
  }
}
</script>
