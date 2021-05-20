<script lang="ts">
  import { Chart } from "frappe-charts";

  export let data;
  export let title;
  export let type;
  export let height;
  export let colors: string[] = undefined;
  export let chart;

  let chartContainer;

  $: {
    chartContainer &&
      (chart = new Chart(chartContainer, {
        data,
        title,
        type,
        height,
        colors,
      }));
  }
</script>

<div bind:this={chartContainer} />
