import React from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

function Chart({ data }) {
  const chartData = {
    labels: ["Income", "Expense"],
    datasets: [
      {
        label: "Amount",
        data: [data.total_income || 0, data.total_expense || 0],
      }
    ]
  };

  return <Bar data={chartData} />;
}

export default Chart;