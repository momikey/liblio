<template>
  <div class="home columns">
    <div class="column is-two-thirds">
      <!-- example post composer -->
      <post-composer />

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
import PostComposer from '@/components/PostComposer.vue'

export default {
  name: 'home',

  components: {
    CreatorPanel,
    CreatorPostCard,
    PostComposer
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
    // this.$http.get('http://localhost:4000/api/users')
    //   .then(response => {
    //     return response.json();
    //   })
    //   .then(json => {
    //     console.log(json);
    //   })
    //   .catch(response => {
    //     console.log(`Error: ${response.body}`);
    //   })
  }
}
</script>
