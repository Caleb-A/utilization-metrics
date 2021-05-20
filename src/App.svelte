<script lang="ts">
  import UtilizationMetricsChart from "./UtilizationMetricsChart.svelte";
  import SelectFileName from "./SelectFileName.svelte";

  let fileName = null;
</script>

<main>
  <div>
    <a href="/">
      <svg focusable="false" viewBox="0 0 24 24" aria-hidden="true"
        ><path
          d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"
        /></svg
      >
    </a>
    <SelectFileName bind:fileName />
  </div>
  {#if fileName}
    <UtilizationMetricsChart {fileName} />
  {/if}
</main>

<style>
  * {
    box-sizing: border-box;
    margin: 0px;
    padding: 0px;
    border: 0px solid black;
    background: transparent;
  }
  :root {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  }

  div {
    display: flex;
  }

  a {
    text-decoration: none;
    display: block;
    width: 100%;
    display: flex;
    background: #2196f3;
    padding: 1em;
    color: black;
    transition-duration: 0.5s;
    width: 4em;
    height: 4em;
    align-items: center;
    justify-content: center;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
  }
  svg {
    background: transparent;
    fill: currentColor;
    height: 1em;
  }
  a:hover {
    background: #9fa8da;
  }

  a:active {
    background: #1a237e;
    color: white;
  }
  span {
    margin-left: auto;
  }
</style>
