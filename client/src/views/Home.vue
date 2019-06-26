<template>
  <div class="home columns">
    <div class="column is-two-thirds">
      <!-- example post composer -->
      <post-composer />

      <!-- exmaple post -->
      <creator-post-card
        :post="testPost"
      />

      <!-- example work -->
      <work-info-card
        :title="testWork.title"
        :description="testWork.description"
        :url="testWork.url"
        :image="testWork.image"
        :tags="testWork.tags"
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
import WorkInfoCard from '@/components/WorkInfoCard.vue'

export default {
  name: 'home',

  components: {
    CreatorPanel,
    CreatorPostCard,
    PostComposer,
    WorkInfoCard
  },

  data () {
    return {
      testPost: {
        author: 'Tester',
        title: "This is a test",
        content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit.
         Phasellus nec iaculis mauris.`,
      },

      testWork: {
        title: 'My test book',
        image: null,
        url: 'https://example.com/my-test-book',
        tags: [
          { key: 'test', value: "Test" },
          { key: 'book', value: "Book" }
        ],
        description: `
          <p>
          This is a test work. This one is intended to be a book, but others could
          be pictures, illustrations, music, or anything creative.
          </p>

          <p>
          Make a bunch of text so your work stands out.
          </p>
        `,
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
