<script lang="ts">
  let fileNames: string[] = [];

  export let fileName;

  fetch("http://localhost:5000/uploads/list")
    .then((v) => v.json())
    .then((v) => {fileNames = v; fileName = fileNames[0]});
</script>

{#if fileNames.length}
  <select bind:value={fileName}>
    {#each fileNames as availableFileName}
      <option value={availableFileName}>{availableFileName}</option>
    {/each}
  </select>
{:else}
  <p>Loading...</p>
{/if}

<style>
  select {
    width: 100%;
    padding: 1em;
    background: #3f51b5;
    color: white;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
  }
  option {
    background: white;
    color: black;
  }
</style>
