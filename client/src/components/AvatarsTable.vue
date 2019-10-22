<template>
  <b-table
    :data="data"
    ref="table"
    :default-sort="['id', 'asc']"
    striped

    paginated
    backend-pagination
    :total="totalPosts"
    :per-page="perPage"
    @page-change="onPageChange"
  >
  </b-table>
</template>

<script>
export default {
    props: [
        'perPage'
    ]
}
</script>

<style>

</style>