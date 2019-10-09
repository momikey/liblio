<template>
    <div class="select">
        <select name="per-page" :value="value" @input="$emit('input', $event.target.value)">
            <option selected>10</option>
            <option>25</option>
            <option>100</option>
        </select>

        per page
    </div>
</template>

<script>
export default {
    props: [
        'value'
    ]
}
</script>