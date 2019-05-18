<template>
  <div class="home columns">
    <div class="column is-two-thirds">
      <img alt="Vue logo" src="../assets/logo.png">
      <p>We'll put posts and things like that over here</p>

      <!-- exmaple post -->
      <creator-post-card
        :post="testPost"
      />
    </div>

    <div class="column is-one-third">
      <creator-panel />
    </div>
  </div>
</template>

<script>
import CreatorPanel from '@/components/CreatorPanel.vue'
import CreatorPostCard from '@/components/CreatorPostCard.vue'

export default {
  name: 'home',

  components: {
    CreatorPanel,
    CreatorPostCard
  },

  data () {
    return {
      testPost: {
        author: 'Tester',
        title: "This is a test",
        content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit.
         Phasellus nec iaculis mauris.`,
      },

      testUser: null,
    }
  },

  mounted () {
    this.$http.get('http://localhost:4000/api/users')
      .then(response => {
        return response.json();
      })
      .then(json => {
        console.log(json);
      })
      .catch(response => {
        console.log(`Error: ${response.body}`);
      })
  }
}
</script>
