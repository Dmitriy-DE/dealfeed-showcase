/**
 * Simplified public example of the ingestion shape.
 */

type Product = {
  sourceId: string;
  title: string;
  priceEur: number;
  discountPct: number;
  affiliateUrl: string;
};

export function filterProducts(products: Product[]): Product[] {
  return products.filter((product) => {
    if (product.priceEur < 5 || product.priceEur > 100) return false;
    if (product.discountPct < 15) return false;

    const url = new URL(product.affiliateUrl);
    return ["example-affiliate.test", "merchant.test"].includes(url.hostname);
  });
}

export function dedupeKey(product: Product): string {
  return [product.sourceId, product.priceEur, product.discountPct].join(":");
}
