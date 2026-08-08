export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { amount, currency, receipt } = req.body;

  try {
    const response = await fetch('https://api.razorpay.com/v1/orders', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Basic ${Buffer.from('rzp_live_TNBnhcTa8wRfRF:qApYB9AaNQAWLlb6Butjy3gh').toString('base64')}`
      },
      body: JSON.stringify({
        amount: Math.round(amount), // Ensure amount is an integer
        currency: currency || 'INR',
        receipt: receipt || `receipt_${Date.now()}`
      })
    });

    const data = await response.json();

    if (!response.ok) {
      console.error('Razorpay Error:', data);
      return res.status(response.status).json(data);
    }

    return res.status(200).json(data);
  } catch (error) {
    console.error('Create order error:', error);
    return res.status(500).json({ error: 'Failed to create order' });
  }
}
