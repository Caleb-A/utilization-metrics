<script>
  import Chart from "./Chart.svelte";
  export let fileName;

  let data = null;

  let chartRef;
  let metrics;

  $: {
    console.log(fileName);
    console.log(`http://localhost:5000/uploads/${fileName}`);
  }
  $: {
    fetch(`http://localhost:5000/uploads/${fileName}`)
      .then((v) => v.text())
      .then((v) => {
        metrics = v
          .split("\n")
          .map((i) => i.split(" "))
          .filter((item) => item.length === 2);
      });
  }

  $: {
    if (metrics) {
      console.log(metrics);
      data = {
        labels: metrics.map((i) => i[0]),
        datasets: [
          {
            values: metrics.map((i) => i[1]),
            truncateLegends: 1,
          },
        ],
      };
    }
  }
</script>

{#if data}
  <Chart {data} type="line" bind:this={chartRef} />
{/if}
